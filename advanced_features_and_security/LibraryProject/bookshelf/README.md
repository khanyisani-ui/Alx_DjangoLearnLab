## Permissions and Groups Setup

### Custom User Model
- `CustomUser`: Extends `AbstractUser` with additional fields `date_of_birth` and `profile_photo`.

### Article Model Permissions
- `can_view`: Can view articles
- `can_create`: Can create articles
- `can_edit`: Can edit articles
- `can_delete`: Can delete articles

### Groups and Assigned Permissions
- `Viewers`: Assigned `can_view` permission.
- `Editors`: Assigned `can_view`, `can_create`, `can_edit` permissions.
- `Admins`: Assigned `can_view`, `can_create`, `can_edit`, `can_delete` permissions.

### Views Permission Enforcement
- `article_list`: Requires `can_view` permission.
- `article_create`: Requires `can_create` permission.
- `article_edit`: Requires `can_edit` permission.
- `article_delete`: Requires `can_delete` permission.

### Testing Permissions
- Create test users and assign them to the appropriate groups.
- Log in as these users and verify that permissions are correctly enforced for each action (viewing, creating, editing, deleting articles).
