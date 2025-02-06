# RecipeDB UI Architecture

## Overview

This document outlines the architecture of the RecipeDB frontend, built with React, Chakra UI, TanStack Query, and Zustand. The architecture emphasizes component reusability, maintainability, and a consistent user experience.

## Core Principles

* **Atomic Design:** Components are categorized into atoms, molecules, organisms, templates, and pages, promoting reusability and maintainability.
* **Component-Driven Development:** Focus on building self-contained, reusable components with clear interfaces.
* **Consistent Styling:** Use theme-based styling with minimal component-level styles.
* **Performance:** Optimize for fast loading times and smooth interactions.
* **Accessibility:** Adhere to WCAG guidelines for inclusivity.

## Component Structure

### 1. Atoms (`/components/atoms`)
Fundamental building blocks with no dependencies:

```
atoms/
├── Button/
│   ├── IconButton.tsx    # Base icon button
│   └── ActionButton.tsx  # Primary action button
├── Input/
│   ├── SearchInput.tsx   # Base search input
│   └── TextInput.tsx     # Base text input
├── Text/
│   ├── Heading.tsx       # Typography components
│   └── Body.tsx
└── Display/
    ├── Badge.tsx         # Status badges
    └── Icon.tsx          # Icon components
```

### 2. Molecules (`/components/molecules`)
Simple combinations of atoms:

```
molecules/
├── Form/
│   ├── SearchBar.tsx     # SearchInput + IconButton
│   └── FilterSelect.tsx  # Select + Label
├── Display/
│   ├── StatDisplay.tsx   # Icon + Text combination
│   └── TagGroup.tsx      # Group of badges
└── Navigation/
    └── Breadcrumb.tsx    # Navigation breadcrumb
```

### 3. Organisms (`/components/organisms`)
Complex components composed of molecules:

```
organisms/
├── Recipe/
│   ├── RecipeCard.tsx    # Complete recipe card
│   ├── RecipeGrid.tsx    # Grid of recipe cards
│   └── RecipeFilters.tsx # Filter panel
├── Layout/
│   ├── Header.tsx        # App header
│   └── Sidebar.tsx       # Navigation sidebar
└── Search/
    └── SearchPanel.tsx   # Complete search interface
```

### 4. Templates (`/components/templates`)
Page layouts that organize organisms:

```
templates/
├── MainLayout.tsx        # Primary app layout
├── RecipeListTemplate.tsx # Recipe listing page layout
└── RecipeDetailTemplate.tsx # Recipe detail page layout
```

### 5. Pages (`/pages`)
Complete pages using templates:

```
pages/
├── RecipeListPage.tsx    # Recipe listing
├── RecipeDetailPage.tsx  # Recipe details
└── SearchPage.tsx        # Search interface
```

## Component Guidelines

### Styling
- Use theme-based styles defined in `/theme`
- No inline styles
- Use CSS modules for component-specific styles
- Leverage Chakra UI's style props for minor adjustments

### Props Interface
```typescript
// Example component structure
interface ComponentProps {
  // Required props first
  id: string;
  title: string;

  // Optional props second
  variant?: 'default' | 'featured';
  onAction?: () => void;

  // Children last
  children?: React.ReactNode;
}
```

### State Management
- Local state: React.useState
- Complex state: Zustand stores
- Server state: TanStack Query
- Theme/UI state: Chakra UI hooks

### Testing
```
__tests__/
├── atoms/
├── molecules/
├── organisms/
└── integration/
```

## Implementation Example

```typescript
// atoms/Button/ActionButton.tsx
import { Button, type ButtonProps } from '@chakra-ui/react';
import styles from './ActionButton.module.css';

interface ActionButtonProps extends ButtonProps {
  label: string;
}

export const ActionButton: React.FC<ActionButtonProps> = ({
  label,
  ...props
}) => (
  <Button
    className={styles.button}
    {...props}
  >
    {label}
  </Button>
);
```

## Migration Strategy

1. Create atomic components first
2. Build molecules using atoms
3. Refactor existing organisms
4. Create templates
5. Update pages

Would you like me to help implement this structure and start migrating your components?
