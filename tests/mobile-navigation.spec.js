const { test, expect } = require('@playwright/test');

test.describe('Mobile Navigation', () => {
  test('should toggle mobile menu when clicking menu button', async ({ page }) => {
    await page.goto('/');
    
    // Verify we're in mobile view by checking if the menu button is visible
    const menuButton = page.locator('#menu-button');
    await expect(menuButton).toBeVisible();
    
    // Initially, the navigation should be hidden (not have nav-open class)
    const siteNav = page.locator('#site-nav');
    await expect(siteNav).not.toHaveClass(/nav-open/);
    
    // Click the menu button to open the navigation
    await menuButton.click();
    
    // After clicking, navigation should have nav-open class
    await expect(siteNav).toHaveClass(/nav-open/);
    
    // Menu button should also have nav-open class
    await expect(menuButton).toHaveClass(/nav-open/);
    
    // Menu button aria-pressed should be true
    await expect(menuButton).toHaveAttribute('aria-pressed', 'true');
    
    // Click again to close
    await menuButton.click();
    
    // Navigation should no longer have nav-open class
    await expect(siteNav).not.toHaveClass(/nav-open/);
    await expect(menuButton).not.toHaveClass(/nav-open/);
    await expect(menuButton).toHaveAttribute('aria-pressed', 'false');
  });
  
  test('should show navigation links when menu is open', async ({ page }) => {
    await page.goto('/');
    
    const menuButton = page.locator('#menu-button');
    const siteNav = page.locator('#site-nav');
    
    // Initially, navigation links might be hidden/not visible in mobile view
    // Click to open
    await menuButton.click();
    
    // Wait for navigation to be open
    await expect(siteNav).toHaveClass(/nav-open/);
    
    // Check that navigation links are accessible
    const navLinks = page.locator('#site-nav .nav-list-link');
    const count = await navLinks.count();
    expect(count).toBeGreaterThan(0);
  });

  test('should keep mobile menu available after scrolling', async ({ page }) => {
    await page.goto('/general/slack/');

    const menuButton = page.locator('#menu-button');
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight / 2));

    await expect(menuButton).toBeVisible();
    await menuButton.click();

    const siteNav = page.locator('#site-nav');
    await expect(siteNav).toHaveClass(/nav-open/);
    await expect(siteNav).toBeVisible();
  });

  test('should show previous and next links on course pages', async ({ page }) => {
    await page.goto('/courses/data-engineering-zoomcamp/');

    const pageNavigation = page.locator('.page-navigation');
    await expect(pageNavigation).toBeVisible();
    await expect(pageNavigation.locator('.page-navigation-previous')).toContainText('Machine Learning Zoomcamp');
    await expect(pageNavigation.locator('.page-navigation-next')).toContainText('Prerequisites');
  });
});
